import SimpleCell, {
    SimpleCellProps,
} from '@vkontakte/vkui/dist/components/SimpleCell/SimpleCell'
import React from 'react'
import { IconsAdapter } from 'shared/components'
import { DESCRIPTION_DEFAULT } from './FavoriteItemCell.const'

/** Компонент единицы списка избранного */
export const FavoriteItemCell: React.FC<
    Pick<SimpleCellProps, 'description'>
> = React.memo(({ children, description = DESCRIPTION_DEFAULT }) => {
    return (
        <SimpleCell
            description={description}
            after={<IconsAdapter iconType={'IconMoreHorizontal'} />}
        >
            {children}
        </SimpleCell>
    )
})
