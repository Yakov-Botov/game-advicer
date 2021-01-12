import React from 'react'
import {Row, RowProps} from 'react-flexbox-grid'

type RowAdapterProps = RowProps

/** Декоратор над компонентом Row для системы grid приложения */
export const RowAdapter: React.FC<RowAdapterProps> = React.memo((props) => {
    return <Row {...props} />
})
