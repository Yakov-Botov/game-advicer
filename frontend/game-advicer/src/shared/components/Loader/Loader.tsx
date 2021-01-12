import PanelSpinner from '@vkontakte/vkui/dist/components/PanelSpinner/PanelSpinner'
import React from 'react'
import { LoaderProps } from './Loader.model'

/** Компонент индикатора загрузки */
export const Loader: React.FC<LoaderProps> = React.memo(
    ({ height = 200, size = 'large', ...otherProps }) => (
        <PanelSpinner height={height} size={size} {...otherProps} />
    )
)
