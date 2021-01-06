import React from 'react'
import {Row, RowProps} from 'react-flexbox-grid'

type RowAdapterProps = RowProps

/** DI обертка над компонентом row для grid приложения  */
export const RowAdapter: React.FC<RowAdapterProps> = React.memo((props) => {
    return <Row {...props} />
})
